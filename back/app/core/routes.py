# core/routes.py
import importlib
import pkgutil
from pathlib import Path
from fastapi import FastAPI
from fastapi import APIRouter

def register_routers(app: FastAPI) -> None:
    modules_path = Path(__file__).parent.parent / "modules"
    
    for module_dir in modules_path.iterdir():
        if not module_dir.is_dir():
            continue
        routes_module = f"app.modules.{module_dir.name}.presentation.routes"
        try:
            mod = importlib.import_module(routes_module)
            if hasattr(mod, "router"):
                app.include_router(mod.router)
        except ModuleNotFoundError:
            pass