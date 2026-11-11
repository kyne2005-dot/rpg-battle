class Character:
    def __init__(self, name="Hero", max_health=200, health=None):
        if max_health <= 0:
            raise ValueError("max_health must be positive")
        if health is None:
            health = max_health
        if not 0 <= health <= max_health:
            raise ValueError("health must be between 0 and max_health")
        self.name = name
        self._max_health = max_health
        self._health = health

    def __str__(self):
        return f"{self.name}: {self._health}/{self._max_health} HP"

    def take_damage(self, amount):
        if amount < 0:
            raise ValueError("Damage cannot be negative")
        self._health = max(0, self._health - amount)

    def heal(self, amount):
        if amount < 0:
            raise ValueError("Healing cannot be negative")
        self._health = min(self._max_health, self._health + amount)

    def is_alive(self):
        return self._health > 0

    @property
    def health(self):
        return self._health

    @property
    def max_health(self):
        return self._max_health