"""Sensor platform for hatch_rest_wifi."""
from homeassistant.components.sensor import SensorEntity

from .const import DEFAULT_NAME, DOMAIN, ICON, SENSOR
from .entity import HatchRestWifiEntity


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices([HatchRestWifiSensor(coordinator, entry)])


class HatchRestWifiSensor(HatchRestWifiEntity, SensorEntity):
    """hatch_rest_wifi Sensor class."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{DEFAULT_NAME}_{SENSOR}"

    @property
    def native_value(self):
        """Return the native value of the sensor."""
        return self.coordinator.data.get("body")

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return ICON
