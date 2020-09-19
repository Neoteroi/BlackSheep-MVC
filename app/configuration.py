from roconfiguration import Configuration


def load_configuration() -> Configuration:
    configuration = Configuration()

    # NB: loads settings from a yaml file, then environment variables
    # refer to https://github.com/RobertoPrevato/roconfiguration documentation
    # for more details.
    configuration.add_yaml_file("settings.yaml")
    configuration.add_environmental_variables()

    return configuration
