<script>
	import { page } from '$app/stores';

	let slug = $page.url.pathname.slice(1);
  let urlString = '';
  let video_media_urls = [];
  let state = '';
  let grab_iframes = false;

  const handleSubmit = async () => {
    let error = false;
    state = 'loading';
    let response = await fetch("http://localhost:8000/extract_video/", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        url: urlString,
        iframe: grab_iframes
      })
    }).then(res => res.json()).catch(() => error = true);
    video_media_urls = response;
    if (error) {
      state = 'error';
    } else {
      state = 'success';
    }
  }
</script>

<h1 class="mb-4 font-mono font-bold text-6xl text-center text-slate-200">{slug}</h1>
<div class="flex flex-col mb-2">
  <input class="w-full p-2 rounded-lg" bind:value={urlString} autocomplete="off" type="text" placeholder="Enter URL here" />
  <div class="flex flex-row justify-start my-1 bg-slate-50 rounded-lg p-2 max-w-fit">
    <input class="mt-1.5" type="checkbox" bind:value={grab_iframes} />
    <p>Grab iframes?</p>
  </div>
  <button type="submit"on:click|preventDefault={handleSubmit} class="mt-2 rounded-lg p-2 text-white bg-purple-400 hover:bg-purple-800">Extract Media URLs</button>
</div>

{#if state == 'loading'}
<p class="my-4 bg-slate-50 p-2 rounded-lg">Fetching Media URLs...</p>
{:else if state == 'error'}
  <p class="my-4 bg-slate-50 p-2 rounded-lg">Error, couldn't fetch</p>
{:else if state == 'success'}
  {#each video_media_urls as video_media_url}
    <div class="my-4 bg-slate-50 p-2 rounded-lg">
      <a class=" break-all" target="new" href={video_media_url}>{video_media_url}</a>
    </div>
  {/each}
{/if}
