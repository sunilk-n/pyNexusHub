import os
import platform
from enum import Enum
import yaml


class Platform(Enum):
    WINDOWS = "windows"
    LINUX = "linux"

    # Not tested on mac systems hence below line is just for reference
    MAC = "darwin"


class Context:
    def __init__(self, template_path: str) -> None:
        config = Config(template_path)
        self.config = config.config

    def _get_context(self, platform_type: Platform = None):
        context_tokens = {}
        if not platform_type:
            current_platform = platform.system()
            if current_platform == "Windows":
                context_platform = Platform.WINDOWS
                env_identifier = "%{}%"
            elif current_platform == "Linux":
                context_platform = Platform.LINUX
                env_identifier = "${}"
            elif current_platform == "Darwin":
                raise Exception("Not tested on mac systems hence this is just for information")
                context_platform = Platform.MAC
                env_identifier = "${}"
            else:
                raise Exception(f"Cannot recognize platform: {current_platform}")
            context_tokens["root"] = self._root_templates[context_platform.value]
        else:
            context_tokens["root"] = self._root_templates[platform_type.value]
        return context_tokens


class Config:
    def __init__(self, template_path: str) -> None:
        self.template_path = template_path
        self.config = self._get_config()

    def __call__(self):
        return self.config

    def _get_config(self):
        with open(self.template_path, 'r') as default_config_file:
            config = yaml.safe_load(default_config_file)
        self._get_packagers(config['root'][platform.system().lower()])
        return config

    def _get_packagers(self, root_path):
        """
        Gets the packager config, for example let's say the default tools path have any folder name in it, then the
        config should have all the folder names as config keys. Under the packager, there will be residing the tool
        names.
        """
        config = {}

    def _get_packager_tools(self, packager_location):
        config = {}
        for package_version in os.listdir(packager_location):
            if os.path.isdir(os.path.join(packager_location, package_version)):
                config[os.path.basename(packager_location)] = package_version
        return config


    def get_tools(self):
        python_tools = self.get_python_tools()

    def get_python_tools(self):
        production_available_tools = os.listdir(os.path.join(self.tool_location, "python"))
        local_available_tools = os.listdir("%USERPROFILE%/tools/python")

    def get_maya_tools(self):
        production_available_tools = os.listdir(os.path.join(self.tool_location, "maya"))
        local_available_tools = os.listdir("%USERPROFILE%/tools/maya")

    def get_nuke_tools(self):
        production_available_tools = os.listdir(os.path.join(self.tool_location, "nuke"))
        local_available_tools = os.listdir("%USERPROFILE%/tools/nuke")


if __name__ == '__main__':
    default_template = {
        "job": "ABC",
        "tools": {
            "studioLibrary": {
                "version": "1.0.0",
                "env_var": "STUDIOLIBRARY_VERSION"
            }
        }
    }
    a = Context(r"I:\exStudio\config.yaml")
    print(a.config)
