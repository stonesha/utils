<script>
	import Heading from '../components/Heading.svelte'

	let url = ''
	let media_urls = []
	let loading = false

	const extractMediaFromUrl = async () => {
		loading = true
		const { videoTags } = await fetch('/api/extract-media-from-url', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				url: url
			})
		}).then((res) => res.json())

		media_urls = videoTags
		loading = false
	}
</script>

<Heading />

<input class="w-full m-2 p-2 rounded-lg" placeholder="URL to extract media from" bind:value={url} />
<div class="flex flex-row justify-center mb-10">
	<button
		on:click|preventDefault={extractMediaFromUrl}
		class="rounded-lg p-2 text-white bg-blue-400 hover:bg-blue-800">Extract Media</button
	>
</div>

{#if loading}
	<div class="flex flex-row justify-center">
		<span class="loader" />
	</div>
{:else}
	{#each media_urls as media_url}
		<a class="w-5/6 m-2 p-2 rounded-lg bg-white truncate" href={media_url} target="_blank">
			{media_url}
		</a>
	{/each}
{/if}

<style>
	.loader {
		width: 48px;
		height: 48px;
		border: 5px solid #fff;
		border-bottom-color: #ff3d00;
		border-radius: 50%;
		display: inline-block;
		box-sizing: border-box;
		animation: rotation 1s linear infinite;
	}

	@keyframes rotation {
		0% {
			transform: rotate(0deg);
		}
		100% {
			transform: rotate(360deg);
		}
	}
</style>
