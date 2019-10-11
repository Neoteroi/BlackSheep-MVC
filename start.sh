#!/bin/bash
# Use this script to start the application with hot reload.

uvicorn server:app --port 44777 --reload --log-level info