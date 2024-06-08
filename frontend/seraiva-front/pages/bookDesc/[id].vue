<script setup>
    const route = useRoute();
    const {data: bookFound} = await useFetch(`https://https://seraiva-somativa-production.up.railway.app/api/auth/book/${route.params.id}`);
</script>

<template>
    <section class="desc-scr">
        <div class="book-inf">
            <div class="book-cape">
                <img :src="bookFound.image" alt="Capa do Livro" width="500" class="blur-img">
                <img :src="bookFound.image" alt="Capa do Livro" width="500">
            </div>
            <br><br>
            <h1>Nome: {{ bookFound.name }}</h1>
            <br>
            <h3>Gênero: {{ bookFound.categoryFK.name }}</h3>
            <br>
            <h3>Preço do Empréstimo: R${{ bookFound.price }}</h3>
            <br>
            <h3>Edição: {{ bookFound.edition}}</h3>
            <br>
            <h3>Data de Lançamento: {{ bookFound.releaseDate }}</h3>
            <br>
            <h3>Quantidade Disponível: {{ bookFound.amount }}</h3>
        </div>
        <div class="book-desc">
            <div class="desc-panel">
                <h1>Descrição / Sinopse:</h1>
                <hr>
                <br>
                <h3>{{ bookFound.description }}</h3>
            </div>
            <Button class="add-button" v-if="bookFound.amount >= 1">Emprestar</Button>
            <Button class="unavailable-button" v-if="bookFound.amount <= 0">Indisponível</Button>
        </div>
    </section>
</template>

<style scoped lang="scss">

    .desc-scr{
        width: 100vw;
        height: 100vh;
        background-color: var(--dark-background-color);
        display: flex;
        flex-direction: row;
    }

    .book-desc{
        height: 100vh;
        width: 50vw;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: space-evenly;
        
        .desc-panel{
            min-height: 80vh;
            max-height: 80vh;
            min-width: 45vw;
            max-width: 45vw;
            background-color: rgb(31, 31, 31);
            box-shadow: 0px 0px 15px white;
            padding: 15px;

            h1{
                color: white;
            }

            h3{
                color: white;
            }
        }

        .add-button{
            margin-top: 30px;
            color: white;
            font-size: large;
            font-weight: bold;
            background-color: black;
            border-radius: 3px;
            border-width: 0;
            width: 75%;
            height: 10%;
            transition: 0.5s;

            &:hover{
                cursor: pointer;
                color: black;
                box-shadow: 0px 0px 15px white;
                background-color: white;
                transform: scale(1.1);
            }

        }

        .unavailable-button{
            margin-top: 30px;
            color: white;
            font-size: large;
            font-weight: bold;
            background-color: black;
            border-radius: 3px;
            border-width: 0;
            width: 75%;
            height: 10%;
            transition: 0.5s;

            &:hover{
                cursor: pointer;
                color: white;
                box-shadow: 0px 0px 15px red;
                background-color: red;
                transform: scale(1.1);
            }

        }
    }

    .book-inf{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 50vw;
        height: 100vh;
        background-color: rgb(31, 31, 31);
        box-shadow: 0px 0px 15px white;

        .book-cape{
            .blur-img{
                width: 339px;
                height: 500px;
                position: absolute;
                filter: blur(15px);
            }
            img{
                width: 339px;
                height: 500px;
                position: relative;
            }
        }

        h1{
            color: white;
            text-shadow: 0px 0px 5px white;
        }

        h3{
            color: white;
            text-shadow: 0px 0px 5px white
        }
    }

</style>