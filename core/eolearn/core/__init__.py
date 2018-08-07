"""
The following objects and functions are the core of eo-learn package
"""

from .feature_types import FeatureType
from .eodata import EOPatch, FileFormat
from .eotask import EOTask, CompositeTask
from .eoworkflow import EOWorkflow, LinearWorkflow, Dependency, WorkflowResults
from .eoexecution import EOExecutor

from .core_tasks import CopyTask, DeepCopyTask, AddFeature, RemoveFeature, SaveToDisk, LoadFromDisk
from .plots import bgr_to_rgb, IndexTracker, PatchShowTask
from .utilities import deep_eq, negate_mask, constant_pad, get_common_timestamps


__version__ = '0.2.0'
