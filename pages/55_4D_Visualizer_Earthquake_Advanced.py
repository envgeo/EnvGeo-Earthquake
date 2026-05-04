#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advanced EnvGeo-Earthquake Streamlit page.

The implementation lives in ``earthquake_utils.py``. Keeping this page thin
prevents duplicated logic across Streamlit pages and makes the earthquake code
easier to test and maintain.
"""

import envgeo_earthquake_utils


if __name__ == "__main__":
    envgeo_earthquake_utils.main()
