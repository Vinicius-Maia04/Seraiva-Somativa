<script setup>
    const route = useRoute();
    const { data: bookInformation} = await useFetch(`http://127.0.0.1:8000/book/`);
</script>

<template>
    <section class="card flex-center">
        <div class="check text-right">
            <Checkbox :binary="true" :readonly="true"/>
        </div>
        <div class="book-image">
            <img :src="bookInformation.image"/>
        </div>
        <div>
            <h4 class="book-name">{{ bookInformation[0].name }}</h4>
        </div>
        <div class="flex flex-row">
            <span class="price-text">Preço: R${{ bookInformation[0].price }}</span>
            <div class="m1-2">
                <label class="quantity"> Qtd. Disponível: </label>
                <span class="quantity">{{ bookInformation[0].amount }}</span>
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
        height: 350px;
        max-height: 350px;
        background-color: rgb(31, 31, 31);
        border-radius: 0.5rem;
        margin: 1.5rem;
        transition: 0.5s;

        &:hover{
            transform: scale(1.1);
            box-shadow: 0px 0px 50px rgb(144, 0, 255);
        }


        .book-image{
            width: 90%;
            height: 55%;
            max-width: 200px;
            max-height: 230px;

            img{
                width: 100%;
                height: 100%;
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
            background-color: black;
            border: 0;
            border-radius: 5px;
            transition: 0.5s;
            cursor: pointer;
            
            &:hover{
                background-color: rgb(144, 0, 255);
                box-shadow: 0px 0px 25px rgb(144, 0, 255);
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