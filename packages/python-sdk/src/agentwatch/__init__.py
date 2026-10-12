"""Compatibility shim for the legacy ``agentwatch`` import path (v0.3.x, ADR-0026).

The package was renamed to :mod:`agentsec_agentwatch`; this shim keeps
``import agentwatch`` and ``from agentwatch.<submodule> import ...`` working across
the v0.3.x window. Importing this package yields :mod:`agentsec_agentwatch`, and
submodule imports (``agentwatch.tracer``, ``agentwatch.spans``, ...) resolve to the
*same* module objects as ``agentsec_agentwatch.*``.
"""

from __future__ import annotations

import importlib
import importlib.abc
import importlib.machinery
import importlib.util
import sys
from types import ModuleType

import agentsec_agentwatch

_LEGACY = __name__
_NEW = "agentsec_agentwatch"

# ``import agentwatch`` yields the renamed package.
sys.modules[_LEGACY] = agentsec_agentwatch


class _LegacyAliasLoader(importlib.abc.Loader):
    """Hand back the already-imported ``agentsec_agentwatch`` submodule unchanged."""

    _CANONICAL_ATTRS = ("__spec__", "__loader__", "__package__")

    def __init__(self, module: ModuleType) -> None:
        self._module = module
        # Import machinery rewrites these on the shared module object; snapshot
        # them so the canonical agentsec_agentwatch.* metadata is restored after.
        self._canonical = {name: getattr(module, name, None) for name in self._CANONICAL_ATTRS}

    def create_module(self, spec: importlib.machinery.ModuleSpec) -> ModuleType:
        return self._module

    def exec_module(self, module: ModuleType) -> None:
        for name, value in self._canonical.items():
            setattr(module, name, value)


class _LegacyAliasFinder(importlib.abc.MetaPathFinder):
    """Map ``agentwatch.<sub>`` onto ``agentsec_agentwatch.<sub>``."""

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> importlib.machinery.ModuleSpec | None:
        if not fullname.startswith(_LEGACY + "."):
            return None
        if fullname == _LEGACY + ".__main__":
            # Let runpy load the real ``__main__`` (the alias loader has no get_code).
            return None
        target_name = _NEW + fullname[len(_LEGACY) :]
        try:
            module = importlib.import_module(target_name)
        except ImportError:
            return None
        return importlib.util.spec_from_loader(fullname, _LegacyAliasLoader(module))


sys.meta_path.insert(0, _LegacyAliasFinder())
