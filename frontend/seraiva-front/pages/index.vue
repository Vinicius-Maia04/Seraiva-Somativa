<script>

</script>

<template>
    <main class="home-container flex-center">
        <h2 class="mt-4 mb-4">Nossa Biblioteca</h2>
        <Toast/>
        <div class="grid align-items-center justify-content-center">
            <div>
                <BookCard/>
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

    .home-container{
        background-color: var(--dark-background-color);
        margin: 0;
        width: 100vw;
        height: 100vh;

        h2{
            color: white;
        }
    }

    .p-toast-summary{
        padding: 1.5rem !important;
    }
</style>