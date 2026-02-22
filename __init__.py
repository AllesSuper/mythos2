from __future__ import annotations

import importlib
import pkgutil

# Alle Module in mythos.commands automatisch importieren,
# damit sie sich in der Registry registrieren können.
package_name = __name__
package = importlib.import_module(package_name)

for m in pkgutil.iter_modules(package.__path__, package_name + "."):
    importlib.import_module(m.name)