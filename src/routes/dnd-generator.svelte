<script lang="ts">
	import { page } from '$app/stores'

	let slug = $page.url.pathname.slice(1)
  let dnd_race: string = ''
  let dnd_class: string = ''
  let dnd_stats = {
    strength: 0,
    strength_modifier: '',
    dexterity: 0,
    dexterity_modifier: '',
    constitution: 0,
    constitution_modifier: '',
    intelligence: 0,
    intelligence_modifier: '',
    wisdom: 0,
    wisdom_modifier: '',
    charisma: 0,
    charisma_modifier: '',
  }
  let rolled = false

   const dnd_data = {
      races: [
          "Dwarf (PBR, PHB, SRD)",
          "Hill Dwarf (PBR, PHB, SRD)",
          "Mountain Dwarf (PHB)",
          "Duergar (SCAG)",
          "Elf (PBR, PHB, SRD)",
          "High Elf (PBR, PHB, SRD)",
          "Wood Elf (PHB)",
          "Dark Elf (Drow) (PHB)",
          "Eladrin (DMG)",
          "Halfling (PBR, PHB, SRD)",
          "Lightfoot Halfling (PBR, PHB, SRD)",
          "Stout Halfling (PHB)",
          "Ghostwise Halfling (SCAG)",
          "Human (PBR, PHB, SRD)",
          "Variant Human (PHB)",
          "Dragonborn (PHB, SRD)",
          "Gnome (PHB, SRD)",
          "Forest Gnome (PHB)",
          "Rock Gnome (PHB, SRD)",
          "Deep Gnome (Svirfneblin) (EE, SCAG)",
          "Half-Elf (PHB, SRD)",
          "Half-Elf Variant",
          "High Elf Descent (SCAG)",
          "Half-Elf Variant",
          "Wood Elf Descent (SCAG)",
          "Half-Elf Variant",
          "Drow Descent (SCAG)",
          "Half-Elf Variant",
          "Aquatic Descent (SCAG)",
          "Half-Orc (PHB, SRD)",
          "Tiefling (PHB, SRD)",
          "Tiefling Variant",
          "Feral (SCAG)",
          "Tiefling Variant",
          "Devil's Tongue (SCAG)",
          "Tiefling Variant",
          "Hellfire (SCAG)",
          "Tiefling Variant",
          "Winged (SCAG)",
          "Aarakocra (EE)",
          "Genasi (EE)",
          "Air Genasi (EE)",
          "Earth Genasi (EE)",
          "Fire Genasi (EE)",
          "Water Genasi (EE)",
          "Goliath (EE, Volo)",
          "Aasimar (Volo, DMG)",
          "Protector Aasimar (Volo)",
          "Scourge Aasimar (Volo)",
          "Fallen Aasimar (Volo)",
          "Firbolg (Volo)",
          "Kenku (Volo)",
          "Lizardfolk (Volo)",
          "Tabaxi (Volo)",
          "Triton (Volo)",
          "Bugbear (Volo)",
          "Goblin (Volo)",
          "Hobgoblin (Volo)",
          "Kobold (Volo)",
          "Orc (Volo)",
          "Yuan-ti Pureblood (Volo)"
      ],
      classes: [
          "Barbarian (PHB, SRD)",
          "Path of the Berserker (PHB, SRD)",
          "Path of the Totem Warrior (PHB)",
          "Bear (PHB)",
          "Eagle (PHB)",
          "Wolf (PHB)",
          "Elk (SCAG)",
          "Tiger (SCAG)",
          "Path of the Battlerager (SCAG)",
          "Path of the Ancestral Guardian (XGtE)",
          "Path of the Storm Herald (XGtE)",
          "Desert (XGtE)",
          "Sea (XGtE)",
          "Tundra (XGtE)",
          "Path of the Zealot (XGtE)",
          "Bard (PHB, SRD)",
          "College of Lore (PHB, SRD)",
          "College of Valor (PHB)",
          "College of Swords (XGtE)",
          "College of Glamour (XGtE)",
          "College of Whispers (XGtE)",
          "College of Satire ()",
          "Cleric (PBR, PHB, SRD)",
          "Knowledge Domain (PHB)",
          "Life Domain (PBR, PHB, SRD)",
          "Light Domain (PHB)",
          "Nature Domain (PHB)",
          "Tempest Domain (PHB)",
          "Trickery Domain (PHB)",
          "War Domain (PHB)",
          "Death Domain (DMG)",
          "Arcana Domain (SCAG)",
          "Forge Domain (XGtE)",
          "Grave Domain (XGtE)",
          "Druid (PHB, SRD)",
          "Circle of the Land (PHB, SRD)",
          "Circle of the Moon (PHB)",
          "Circle of Dreams (XGtE)",
          "Circle of the Shepherd (XGtE)",
          "Fighter (PBR, PHB, SRD)",
          "Champion (PBR, PHB, SRD)",
          "Battle Master (PHB)",
          "Eldritch Knight (PHB)",
          "Purple Dragon Knight (Banneret) (SCAG)",
          "Arcane Archer (XGtE)",
          "Cavalier (XGtE)",
          "Samurai (XGtE)",
          "Monk (PHB, SRD)",
          "Way of the Open Hand (PHB, SRD)",
          "Way of Shadow (PHB)",
          "Way of the Four Elements (PHB)",
          "Way of the Long Death (SCAG)",
          "Way of the Sun Soul (SCAG, XGtE)",
          "Way of the Drunken Master (XGtE)",
          "Way of the Kensei (XGtE)",
          "Paladin (PHB, SRD)",
          "Oath of Devotion (PHB, SRD)",
          "Oath of the Ancients (PHB)",
          "Oath of Vengeance (PHB)",
          "Oathbreaker (DMG)",
          "Oath of the Crown (SCAG)",
          "Oath of Conquest (XGtE)",
          "Oath of Redemption (XGtE)",
          "Ranger (PHB, SRD)",
          "Hunter (PHB, SRD)",
          "Beast Master (PHB)",
          "Gloom Stalker (XGtE)",
          "Horizon Walker (XGtE)",
          "Monster Slayer (XGtE)",
          "Rogue (PBR, PHB, SRD)",
          "Thief (PBR, PHB, SRD)",
          "Assassin (PHB)",
          "Arcane Trickster (PHB)",
          "Swashbuckler (SCAG, XGtE)",
          "Mastermind (SCAG, XGtE)",
          "Inquisitive (XGtE)",
          "Scout (XGtE)",
          "Sorcerer (PHB, SRD)",
          "Draconic Bloodline (PHB, SRD)",
          "Wild Magic (PHB)",
          "Storm Sorcery (SCAG, XGtE)",
          "Divine Soul (XGtE)",
          "Shadow Magic (XGtE)",
          "Warlock (PHB, SRD)",
          "Archfey (PHB)",
          "Fiend (PHB, SRD)",
          "Great Old One (PHB)",
          "The Undying (SCAG)",
          "The Celestial (XGtE)",
          "The Hexblade (XGtE)",
          "Wizard (PBR, PHB, SRD)",
          "Abjuration (PHB)",
          "Conjuration (PHB)",
          "Divination (PHB)",
          "Enchantment (PHB)",
          "Evocation (PBR, PHB, SRD)",
          "Illusion (PHB)",
          "Necromancy (PHB)",
          "Transmutation (PHB)",
          "Bladesinging (SCAG)",
          "War Magic (XGtE)"
      ]
  }

  const generateRace = () => {(dnd_race = dnd_data.races[Math.floor(Math.random() * dnd_data.races.length)])}

  const generateClass = () => {(dnd_class = dnd_data.classes[Math.floor(Math.random() * dnd_data.classes.length)])}

  const determineModifier = (total) => {
    if (total === 3) {
      return -4
    } else if (total === 4 || total === 5) {
      return -3
    } else if (total === 6 || total === 7) {
      return -2
    } else if (total === 8 || total === 9) {
      return -1
    } else if (total === 10 || total === 11) {
      return 0
    } else if (total === 12 || total === 13) {
      return 1
    } else if (total === 14 || total === 15) {
      return 2
    } else if (total === 16 || total === 17) {
      return 3
    } else if (total === 18) {
      return 4
    }
  }

  const generateStats = () => {
    const randomDiceRoll = () => Math.floor(Math.random() * 6) + 1

    for (let i = 0; i < 6; i++) {
      let rolls = [];
      for (let j = 0; j < 4; j++) {
        rolls.push(randomDiceRoll())
      }

      // drop lowest roll
      rolls.sort((a, b) => a - b)
      rolls.pop()

      // add rolls to total
      const total = rolls.reduce((a, b) => a + b)
      const modifier = determineModifier(total) > 0 ? `+${determineModifier(total)}` : determineModifier(total).toString()

      // ugly way to add stats to object
      switch(i) {
        case 0:
          dnd_stats.strength = total
          dnd_stats.strength_modifier = modifier
          break
        case 1:
          dnd_stats.dexterity = total
          dnd_stats.dexterity_modifier = modifier
          break
        case 2:
          dnd_stats.constitution = total
          dnd_stats.constitution_modifier = modifier
          break
        case 3:
          dnd_stats.intelligence = total
          dnd_stats.intelligence_modifier = modifier
          break
        case 4:
          dnd_stats.wisdom = total
          dnd_stats.wisdom_modifier = modifier
          break
        case 5:
          dnd_stats.charisma = total
          dnd_stats.charisma_modifier = modifier
          break
      }
    }

    rolled = true
  }

  const generateEverything = () => {
    generateRace()
    generateClass()
    generateStats()
  }

</script>

<h1 class="mb-4 font-mono font-bold text-6xl text-center text-slate-200">{slug}</h1>
<div class="flex flex-row justify-around">
  <button
    on:click|preventDefault={generateEverything}
    class="rounded-lg p-2 text-white bg-red-400 hover:bg-red-800">Random Everything</button
  >
</div>
<div class="grid grid-cols-2 content-around m-2 gap-x-4">
  <button
    on:click|preventDefault={generateRace}
    class="rounded-lg p-2 text-white bg-purple-400 hover:bg-purple-800">
    Random Race
  </button>
  <button
    on:click|preventDefault={generateClass}
    class="rounded-lg p-2 text-white bg-teal-400 hover:bg-teal-800">
    Random Class
  </button>
  {#if dnd_race}
    <p class="bg-slate-50 rounded-lg p-2 m-2 text-center">
      {dnd_race}
    </p>
  {:else}
    <p class="p-2 m-2" />
  {/if}

  {#if dnd_class}
    <p class="bg-slate-50 rounded-lg p-2 m-2 text-center">
      {dnd_class}
    </p>
  {:else}
    <p class="p-2 m-2" />
  {/if}

</div>
    

<div class="flex flex-col">
	<button 
    on:click|preventDefault={generateStats}
    class="rounded-lg p-2 text-white bg-blue-400 hover:bg-blue-800"
  >
    Random Stats
  </button>
  {#if rolled}
    <div class="flex flex-row justify-around">
      <p class="bg-slate-50 rounded-lg p-2 m-2 text-center">{dnd_stats.strength} ({dnd_stats.strength_modifier})</p>
      <p class="bg-slate-50 rounded-lg p-2 m-2 text-center">{dnd_stats.dexterity} ({dnd_stats.dexterity_modifier})</p>
      <p class="bg-slate-50 rounded-lg p-2 m-2 text-center">{dnd_stats.constitution} ({dnd_stats.constitution_modifier})</p>
      <p class="bg-slate-50 rounded-lg p-2 m-2 text-center">{dnd_stats.intelligence} ({dnd_stats.intelligence_modifier})</p>
      <p class="bg-slate-50 rounded-lg p-2 m-2 text-center">{dnd_stats.wisdom} ({dnd_stats.wisdom_modifier})</p>
      <p class="bg-slate-50 rounded-lg p-2 m-2 text-center">{dnd_stats.charisma} ({dnd_stats.charisma_modifier})</p>
    </div>
  {/if}
</div>
