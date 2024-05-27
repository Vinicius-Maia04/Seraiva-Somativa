<script>
    const route = useRoute();
    const {data: bookFound} = await useFetch(`http://127.0.0.1:8000/book/${route.params.id}`);
</script>

<template>
    <section class="desc-scr">

    </section>
</template>

<style>

    .desc-scr{
        width: 100vw;
        height: 100vh;
        background-color: var(--dark-background-color);
    }

</style>