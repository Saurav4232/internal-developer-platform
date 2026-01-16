if env not in ["dev", "staging", "prod"]:
    print(f"Invalid environment: {env}")
    sys.exit(1)
