from .jgo import resolve_dependencies, jgo_main as main
from .util import main_from_endpoint, maven_scijava_repository, add_jvm_args_as_necessary
from .version_info import _version as version

__version__ = str(version)
