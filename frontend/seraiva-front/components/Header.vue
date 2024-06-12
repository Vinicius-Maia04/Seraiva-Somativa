<script setup lang="ts">
import { ref } from "vue";

const itensMenu = ref([
  {
    label: "Home",
    icon: "pi pi-home",
  },
  {
    label: "Pagamentos",
    icon: "pi pi-wallet",
  },
  {
    label: "Meus pedidos",
    icon: "pi pi-briefcase",
  },
]);
</script>

<template>
  <header>
    <div class="main-header">
        <div>
            <NuxtLink to="/">
                <h1>Livros</h1>
            </NuxtLink>
        </div>
        <div>
            <NuxtLink to="/login">
                <h1>Login</h1>
            </NuxtLink>
        </div>
        <div>
            <NuxtLink to="/carrinho">
                <h1>Carrinho</h1>
            </NuxtLink>
        </div>
    </div>
  </header>
</template>

<style scoped lang="scss">
    .main-header{
        display: flex;
        flex-direction: row;
        justify-content: space-evenly;
        justify-items: center;
        background-color: black;
        height: var(--altura-header);

        h1{
            color: white;
            text-decoration: none;
        }
    }
</style>