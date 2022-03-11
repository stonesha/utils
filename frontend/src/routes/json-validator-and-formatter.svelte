<script>
  import { page } from '$app/stores'

  let jsonString = ''
  let slug = $page.url.pathname.slice(1)

  let valid;
  let showValidMessage = false

  const validateJson = () => {
    try {
      JSON.parse(jsonString)
      valid = true
    } catch (e) {
      valid = false
    }
    showValidMessage = true
  }

  const prettifyJson = () => {
    try {
      const prettifiedJson = JSON.stringify(JSON.parse(jsonString), undefined, 4)
      jsonString = prettifiedJson
      valid = true
    } catch (e) {
      valid = false
      showValidMessage = true
    }
  }
</script>

<h1 class="mb-4 font-mono font-bold text-6xl text-center text-slate-200">{slug}</h1>
<div class="flex flex-row w-full justify-around my-4">
  <button on:click|preventDefault={validateJson} class="rounded-lg p-2 text-white bg-purple-400 hover:bg-purple-800">Validate</button>
  <button on:click|preventDefault={prettifyJson} class="rounded-lg p-2 text-white bg-blue-400 hover:bg-blue-800">Prettify</button>
</div>

{#if showValidMessage}
<p class="w-full text-center m-2">{valid ? "Valid JSON String" : "Not a valid JSON"}</p>
{:else}
<p></p>
{/if}

<textarea class="w-full h-96 rounded p-2 border-2 border-gray-100" bind:value={jsonString} placeholder="Put JSON here"></textarea>