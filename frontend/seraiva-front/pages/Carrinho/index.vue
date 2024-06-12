<script>
    definePageMeta({
        middleware: 'auth'
    })
</script>

<template>
    <section class="screen-1">
        <img class="carrinho-blur" src="https://images.uncyc.org/pt/7/7c/Os_carrinhos.jpg">
        <img class="carrinho" src="https://images.uncyc.org/pt/7/7c/Os_carrinhos.jpg">
    </section>
</template>

<style scoped lang="scss">

    .flex-center{
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: center;
    }

    .screen-1{
        align-items: center;
        justify-content: center;
        flex-direction: column;
        display: flex;
        width: 100vw;
        height: 94.7vh;
        background-color: var(--dark-background-color);

        .carrinho{
        width: 25%;
        height: 75%;
        background-color: white;
        position: absolute;
        }

        .carrinho-blur{
        width: 25%;
        height: 75%;
        background-color: white;
        position: relative;
        filter: blur(50px);
        }
    }

</style>