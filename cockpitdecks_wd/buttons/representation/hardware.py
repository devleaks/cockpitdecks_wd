"""
Special represenations for web decks, to draw a "hardware" button

Note: An «Hardware Representation» is an image, an icon.
"""

from cockpitdecks.buttons.representation.hardware import HardwareRepresentation, NO_ICON


class HardwareRepresentationTemplate(HardwareRepresentation):
    """ """

    REPRESENTATION_NAME = "hardware-representation-template"

    def __init__(self, button: "Button"):
        button._config[NO_ICON] = True
        HardwareRepresentation.__init__(self, button=button)

        self.hardware = self.button._def.hardware_representation

    def get_image(self):
        """
        Helper function to get button image and overlay label on top of it.
        Label may be updated at each activation since it can contain datarefs.
        Also add a little marker on placeholder/invalid buttons that will do nothing.
        """
        return None

    def describe(self) -> str:
        return "Template representation for hardware parts."
