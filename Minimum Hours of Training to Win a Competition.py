def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        required_experience = 0
        if sum(energy) >= initialEnergy:
            required_energy = sum(energy) - initialEnergy + 1
        else:
            required_energy = 0
        for i in range(len(experience)):
            if initialExperience > experience[i]:
                initialExperience += experience[i]
            else:
                required_experience += (experience[i] - initialExperience + 1)
                initialExperience += (experience[i] - initialExperience + 1) + experience[i]
        return (required_energy + required_experience)
