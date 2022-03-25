<script>
	import { page } from '$app/stores'
	let slug = $page.url.pathname.slice(1)
</script>

<div class="flex flex-row justify-center">
	{#if slug == ''}
		<h1
			class="mb-4 font-mono font-bold text-2xl sm:text-4xl md:text-6xl text-center text-slate-200"
		>
			utils.stonesha.com
		</h1>
	{:else}
		<a
			href="/"
			class="mb-4 font-mono font-bold text-2xl sm:text-4xl md:text-6xl text-center text-slate-200"
		>
			{'<'}
		</a>
		<h1
			class="mb-4 font-mono font-bold text-2xl sm:text-4xl md:text-6xl text-center text-slate-200"
		>
			&nbsp;{slug}
		</h1>
	{/if}
</div>
