class Hero:
    def __init__(self,name="Hero",max_health=200,health=None):
        if max_health<=0:
            raise ValueError("Needs to be positive")
        if health is None:
            health=max_health
        if not 0<=health<=max_health:
            raise ValueError("Needs to be a number between 0 and max health")
        self._name=name
        self._max_health=max_health
        self._health=health

    def __str__(self) -> str:
        return f"The {self._name} has {self._health}/{self._max_health} health left"

    def damage(self,amount):
        if amount<0:
            raise ValueError("Needs to be positive")
        self._health=max(0,self._health-amount)
    def heals(self,amount):
        if amount<0:
            raise ValueError("Needs to be positive")
        self._health=min(self._max_health,self._health+amount)
    def is_alive(self):
        return self._health>0

    @property
    def health(self):
        return self._health

    @property
    def max_health(self):
        return self._max_health