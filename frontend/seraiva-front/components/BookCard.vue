<script setup>
    
    const prop = defineProps({
        index: {type: String}
    })

    const { data: bookInformation} = await useFetch(`http://127.0.0.1:8000/book/${prop.index}`);
</script>

<template>
    <section class="card flex-center">
        <div class="check text-right">
            <Checkbox :binary="true" :readonly="true"/>
        </div>
        <div class="book-image">
            <nuxt-link :to="`/bookDesc/${bookInformation.id}`">
                <img :src="bookInformation.image"/>
            </nuxt-link>
        </div>
        <div>
            <h4 class="book-name">{{ bookInformation.name }}</h4>
        </div>
        <div class="flex flex-row">
            <span class="price-text">Preço: R${{ bookInformation.price }}</span>
            <div class="m1-2">
                <label class="quantity"> Qtd. Disponível: </label>
                <span class="quantity">{{ bookInformation.amount }}</span>
            </div>
        </div>
        <Button class="add-button">Emprestar</Button>
    </section>
</template>

<style scoped lang="scss">

    .flex-center{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    .card{
        width: 300px;
        max-width: 300px;
        height: 400px;
        max-height: 400px;
        background-color: rgb(31, 31, 31);
        border-radius: 0.5rem;
        margin: 1.5rem;
        transition: 0.5s;

        &:hover{
            transform: scale(1.1);
            box-shadow: 0px 0px 50px white;
        }


        .book-image{
            width: fit-content;
            height: fit-content;

            img{
                width: 136px;
                height: 200px;
            }
        }

        .book-name{
            margin: 0.5rem;
            color: white;
        }

        .add-button{
            width: 80%;
            height: 2rem;
            margin: 1rem;
            color: white;
            font-weight: bold;
            background-color: black;
            border: 0;
            border-radius: 5px;
            transition: 0.5s;
            cursor: pointer;
            
            &:hover{
                color: black;
                font-weight: bold;
                background-color: white;
                box-shadow: 0px 0px 25px white;
            }
        }

        .check{
            width: 95%;
        }

        .price-text{
            color: white;
        }

        .quantity{
            color: white;
        }
    }
</style>