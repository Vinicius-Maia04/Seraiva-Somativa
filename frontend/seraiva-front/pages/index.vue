<script setup>
    const { data: bookInformation} = await useFetch(`http://127.0.0.1:8000/book/`);
</script>

<template>
    <main class="home-container flex-center">
        <h2 class="mt-4 mb-4">Nossa Biblioteca</h2>
        <div class="lib">
            <div v-for="b in bookInformation" :key="b.id">
                <BookCard :index="b.id"/>
            </div>
        </div>
    </main>
</template>

<style scoped lang="scss">

    .flex-center{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-around;
    }

    .lib{
        display: flex;
        flex-direction: row;
        justify-content: space-between;
    }

    .home-container{
        background-color: var(--dark-background-color);
        margin: 0;
        width: 100vw;
        height: 100vh;

        h2{
            color: white;
        }
    }
</style>