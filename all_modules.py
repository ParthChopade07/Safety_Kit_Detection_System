"""
Safety Kit Detection System - Complete Module Manager
Centralized imports for all modules used across the project

Usage:
    Method 1 - Import specific modules:
        from all_modules import cv2, np, YOLO, Path
    
    Method 2 - Import as module:
        import all_modules as mod
        mod.cv2.imread('image.jpg')
    
    Method 3 - Import everything:
        from all_modules import *
"""

import os
import sys
import subprocess
import shutil
import random
import time
import json
import threading
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Optional
from collections import deque


# OpenCV - Main library for image/video processing
try:
    import cv2
    CV2_AVAILABLE = True
except ImportError:
    cv2 = None
    CV2_AVAILABLE = False
    print("⚠️  OpenCV not installed. Install: pip install opencv-python")

# NumPy - Numerical operations and arrays
try:
    import numpy as np
    NUMPY_AVAILABLE = True
except ImportError:
    np = None
    NUMPY_AVAILABLE = False
    print("⚠️  NumPy not installed. Install: pip install numpy")

# Pillow - Image operations for GUI
try:
    from PIL import Image, ImageTk
    PIL_AVAILABLE = True
except ImportError:
    Image = None
    ImageTk = None
    PIL_AVAILABLE = False
    print("⚠️  Pillow not installed. Install: pip install Pillow")

# Scikit-Image - Advanced image processing
try:
    from skimage import filters, exposure, morphology
    import skimage
    SKIMAGE_AVAILABLE = True
except ImportError:
    skimage = None
    filters = None
    exposure = None
    morphology = None
    SKIMAGE_AVAILABLE = False
    print("⚠️  scikit-image not installed. Install: pip install scikit-image")

# IMUtils - Convenience functions for OpenCV
try:
    import imutils
    IMUTILS_AVAILABLE = True
except ImportError:
    imutils = None
    IMUTILS_AVAILABLE = False
    print("⚠️  imutils not installed. Install: pip install imutils")



# PyTorch - Deep learning framework
try:
    import torch
    import torchvision
    TORCH_AVAILABLE = True
except ImportError:
    torch = None
    torchvision = None
    TORCH_AVAILABLE = False
    print("⚠️  PyTorch not installed. Install: pip install torch torchvision")

# Ultralytics YOLO - Object detection
try:
    from ultralytics import YOLO
    YOLO_AVAILABLE = True
except ImportError:
    YOLO = None
    YOLO_AVAILABLE = False
    print("⚠️  Ultralytics not installed. Install: pip install ultralytics")


# Tkinter - GUI toolkit
try:
    import tkinter as tk
    from tkinter import ttk, messagebox
    TKINTER_AVAILABLE = True
except ImportError:
    tk = None
    ttk = None
    messagebox = None
    TKINTER_AVAILABLE = False
    print("⚠️  Tkinter not available (usually comes with Python)")



# YAML - Configuration files
try:
    import yaml
    YAML_AVAILABLE = True
except ImportError:
    yaml = None
    YAML_AVAILABLE = False
    print("⚠️  PyYAML not installed. Install: pip install PyYAML")

# Requests - HTTP library
try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    requests = None
    REQUESTS_AVAILABLE = False
    print("⚠️  Requests not installed. Install: pip install requests")


# Safety equipment classes
SAFETY_CLASSES = {
    'helmet': 0,
    'vest': 1,
    'gloves': 2,
    'safety_glasses': 3,
    'person': 4
}

# Class names list
CLASS_NAMES = ['helmet', 'vest', 'gloves', 'safety_glasses', 'person']

# Default model paths
DEFAULT_MODEL_PATHS = {
    'yolov8n': 'yolov8n.pt',
    'yolov8s': 'yolov8s.pt',
    'yolov8m': 'yolov8m.pt',
    'yolov8l': 'yolov8l.pt',
    'yolov8x': 'yolov8x.pt'
}

# Detection thresholds
DEFAULT_CONFIDENCE_THRESHOLD = 0.5
DEFAULT_IOU_THRESHOLD = 0.5
DEFAULT_IMAGE_SIZE = 640



def check_imports():
    """
    Check which modules are available
    
    Returns:
        dict: Status of each module
    """
    status = {
        'opencv': CV2_AVAILABLE,
        'numpy': NUMPY_AVAILABLE,
        'pillow': PIL_AVAILABLE,
        'skimage': SKIMAGE_AVAILABLE,
        'imutils': IMUTILS_AVAILABLE,
        'torch': TORCH_AVAILABLE,
        'yolo': YOLO_AVAILABLE,
        'tkinter': TKINTER_AVAILABLE,
        'yaml': YAML_AVAILABLE,
        'requests': REQUESTS_AVAILABLE
    }
    return status

def print_import_status():
    """Print the status of all imports"""
    print("=" * 70)
    print("MODULE IMPORT STATUS")
    print("=" * 70)
    
    status = check_imports()
    
    critical = ['opencv', 'numpy', 'yolo']
    optional = ['pillow', 'skimage', 'imutils', 'torch', 'tkinter', 'yaml', 'requests']
    
    print("\nCritical Modules (Required):")
    for module in critical:
        status_str = "✓" if status[module] else "✗"
        print(f"  {status_str} {module}")
    
    print("\nOptional Modules:")
    for module in optional:
        status_str = "✓" if status[module] else "✗"
        print(f"  {status_str} {module}")
    
    print("=" * 70)
    
    if all(status[m] for m in critical):
        print("✅ All critical modules available - System ready!")
    else:
        print("⚠️  Some critical modules missing - Install with: pip install -r requirements.txt")

def get_missing_imports():
    """
    Get list of missing imports
    
    Returns:
        list: Names of missing modules
    """
    status = check_imports()
    missing = [module for module, available in status.items() if not available]
    return missing

def install_missing():
    """Install missing modules"""
    missing = get_missing_imports()
    
    if not missing:
        print("✅ All modules already installed!")
        return True
    
    print(f"Installing missing modules: {', '.join(missing)}")
    print("\nRunning: pip install -r requirements.txt")
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Installation complete!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Installation failed: {e}")
        return False



__all__ = [
    # Standard library
    'os', 'sys', 'subprocess', 'shutil', 'random', 'time', 'json', 'threading',
    'Path', 'datetime', 'Dict', 'List', 'Tuple', 'Optional', 'deque',
    
    # Computer Vision
    'cv2', 'np', 'Image', 'ImageTk', 'skimage', 'filters', 'exposure', 
    'morphology', 'imutils',
    
    # Machine Learning
    'torch', 'torchvision', 'YOLO',
    
    # GUI
    'tk', 'ttk', 'messagebox',
    
    # Data Processing
    'yaml', 'requests',
    
    # Constants
    'SAFETY_CLASSES', 'CLASS_NAMES', 'DEFAULT_MODEL_PATHS',
    'DEFAULT_CONFIDENCE_THRESHOLD', 'DEFAULT_IOU_THRESHOLD', 'DEFAULT_IMAGE_SIZE',
    
    # Availability flags
    'CV2_AVAILABLE', 'NUMPY_AVAILABLE', 'PIL_AVAILABLE', 'SKIMAGE_AVAILABLE',
    'IMUTILS_AVAILABLE', 'TORCH_AVAILABLE', 'YOLO_AVAILABLE', 'TKINTER_AVAILABLE',
    'YAML_AVAILABLE', 'REQUESTS_AVAILABLE',
    
    # Utility functions
    'check_imports', 'print_import_status', 'get_missing_imports', 'install_missing'
]



if __name__ == "__main__":
    print("=" * 70)
    print("ALL MODULES - Safety Kit Detection System")
    print("=" * 70)
    print("\nThis file provides centralized imports for the entire project.")
    print("\nUsage in your code:")
    print("  from all_modules import cv2, np, YOLO, Path")
    print("\nChecking module availability...")
    print()
    print_import_status()
    
    missing = get_missing_imports()
    if missing:
        print(f"\n⚠️  Missing modules: {', '.join(missing)}")
        response = input("\nInstall missing modules now? (y/n): ")
        if response.lower() == 'y':
            install_missing()
    else:
        print("\n✅ All modules are installed and ready to use!")
