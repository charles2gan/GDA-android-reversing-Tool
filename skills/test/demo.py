#!/usr/bin/env python3
"""
Demo script for the GDA Skills project.
This script demonstrates how to use the GDASkillExecutor to analyze APK files.
"""

import json
import os
from gda_skills import GDASkillExecutor


def main():
    print("GDA Skills Demo")
    print("=" * 50)

    # Create an executor instance
    executor = GDASkillExecutor(gda_exe_path="GDA.exe")  # Adjust path as needed

    # Check if sample APK exists
    sample_apk = "2.apk"
    if not os.path.exists(sample_apk):
        print(f"Sample APK '{sample_apk}' not found!")
        return

    try:
        # Start the GDA server with the sample APK
        print("\n1. Starting GDA server...")
        result = executor.execute_skill("apk_start_server", {
            "apk_file": sample_apk,
            "port": 8888
        })
        print(f"Result: {result}")

        # Wait a moment for the server to fully initialize
        import time
        time.sleep(2)

        # Get basic information about the APK
        print("\n2. Getting basic APK information...")
        result = executor.execute_skill("apk_binfo", {})
        print(f"Result: {result}")

        # Get the package name
        print("\n3. Getting package name...")
        result = executor.execute_skill("apk_pname", {})
        print(f"Result: {result}")

        # Get permissions
        print("\n4. Getting permissions...")
        result = executor.execute_skill("apk_permission", {})
        print(f"Result: {result}")

        # Get attack surface
        print("\n5. Getting attack surface...")
        result = executor.execute_skill("apk_attsf", {})
        print(f"Result: {result}")

        # Get URIs
        print("\n6. Getting URIs...")
        result = executor.execute_skill("apk_uri", {})
        print(f"Result: {result}")

        # Get certificates
        print("\n7. Getting certificates...")
        result = executor.execute_skill("apk_cert", {})
        print(f"Result: {result}")

        # Scan for malicious behavior
        print("\n8. Scanning for malicious behavior...")
        result = executor.execute_skill("apk_malscan", {})
        print(f"Result: {result}")

        # Find sensitive information
        print("\n9. Finding sensitive information...")
        result = executor.execute_skill("apk_sensinf", {})
        print(f"Result: {result}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Always stop the server when done
        print("\n10. Stopping GDA server...")
        result = executor.execute_skill("apk_stop_server", {})
        print(f"Result: {result}")

    print("\nDemo completed!")


def list_available_skills():
    """Print all available skills from the skills.json file."""
    print("Available Skills:")
    print("-" * 20)
    
    try:
        with open('skills.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        for skill in data['skills']:
            print(f"- {skill['name']}: {skill['description']}")
    except FileNotFoundError:
        print("skills.json file not found!")
    except json.JSONDecodeError:
        print("Error parsing skills.json file!")


if __name__ == "__main__":
    print("Listing available skills...")
    list_available_skills()
    print()
    
    main()