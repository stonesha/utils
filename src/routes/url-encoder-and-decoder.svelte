<script>
  import {page} from '$app/stores'

  let slug = $page.url.pathname.slice(1)
  let urlString = '';

  const encodeUrl = () => {
    const encodedUri = encodeURI(urlString);
    urlString = encodedUri;
  }

  const decodeUrl = () => {
    const decodedUri = decodeURI(urlString);
    urlString = decodedUri;
  }

</script>

<h1 class="mb-4 font-mono font-bold text-6xl text-center text-slate-200">{slug}</h1>
<div class="flex flex-row w-full justify-around my-4">
	<button
		on:click|preventDefault={encodeUrl}
		class="rounded-lg p-2 text-white bg-purple-400 hover:bg-purple-800">Encode URL</button
	>
	<button
		on:click|preventDefault={decodeUrl}
		class="rounded-lg p-2 text-white bg-blue-400 hover:bg-blue-800">Decode URL</button
	>
</div>
<textarea
	class="w-full h-96 rounded p-2 border-2 border-gray-100"
	bind:value={urlString}
	placeholder="Put URL here"
/>


