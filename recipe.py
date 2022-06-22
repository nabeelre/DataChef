class Recipe():
    def __init__(self):
        self.ingredients = []
        self.mixings = []
        self.noises = []

    def add_ingredient(self, ingredient, mixing):
        self.ingredients.append(ingredient)
        self.mixings.append(mixing)

    def add_noise(self, noise, mixing):
        self.noises.append(noise)
        self.mixings.append(mixing)

    def cook_recipe(self, grid):
        """"Cooks up a recipe."""
        base = np.zeros_like(grid)
        noise_base = np.zeros_like(grid)

        for ing in self.ingredients :
            base += ing.eval(grid)

        for noise in self.noises:
            noise_base += noise.eval(grid)
            
        return base + noise_base