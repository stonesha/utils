<script>
	import Heading from '../components/Heading.svelte'

	let text = ''

	const convertUpper = () => {
		const upperText = text.toUpperCase()
		text = upperText
	}

	const convertLower = () => {
		const lowerText = text.toLowerCase()
		text = lowerText
	}

	const convertCapitalize = () => {
		//capitalize each word in the text
		const capitalizedText = text.replace(/\w\S*/g, function (txt) {
			return txt.charAt(0).toUpperCase() + txt.substring(1).toLowerCase()
		})
		text = capitalizedText
	}
</script>

<Heading />

<div class="flex flex-row w-full justify-around my-4">
	<button
		on:click|preventDefault={convertUpper}
		class="rounded-lg p-2 text-white bg-purple-400 hover:bg-purple-800">UPPERCASE</button
	>
	<button
		on:click|preventDefault={convertLower}
		class="rounded-lg p-2 text-white bg-blue-400 hover:bg-blue-800">lowercase</button
	>
	<button
		on:click|preventDefault={convertCapitalize}
		class="rounded-lg p-2 text-white bg-purple-400 hover:bg-purple-800">Capital Case</button
	>
</div>
<textarea
	class="w-full h-96 rounded p-2 border-2 border-gray-100"
	bind:value={text}
	placeholder="Put text here"
/>
