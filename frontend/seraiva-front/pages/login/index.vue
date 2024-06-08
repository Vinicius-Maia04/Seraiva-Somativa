<script setup lang="ts">
    import { reactive } from 'vue';
    const credentials = reactive({
        email: '',
        password: ''
    });

    const submitLogin = () => {
        console.log('Login: ', credentials);
    }

</script>

<template>
    <section class="screen-1">
        <section class="login-panel">
            <div class="login-content flex-center" >
                <div class="logo">
                    <img class="blur" src="/public/Seraiva.png" width="350" height="154">
                    <img class="img-1" src="/public/Seraiva.png" width="350" height="154">
                </div>
                <h1>Seraiva</h1>
                <form class="login-form">
                    <div class="input-container">
                        <CustomInput v-model="credentials.email" type="email" label="LOGIN" inputId="user-login"/>
                    </div>
                    <div class="input-container">
                        <CustomInput v-model="credentials.password" type="password" label="SENHA" inputId="pass-login"/>
                    </div>
                    <button @click="submitLogin" class="customButtom">Entrar</button>
                </form>
            </div>
        </section>
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
        height: 100vh;
        background-color: var(--dark-background-color);

        .login-panel{
        width: 25%;
        height: 75%;
        background-color: white;

            .login-content{
                flex-direction: column;
                width: 100%;
                height: 80%;

                .logo{
                    align-items: center;
                    justify-content: center;
                    flex-direction: row;
                    display: flex;

                    .blur{
                        position: relative;
                        filter: blur(15px);
                    }

                    .img-1{
                        position: absolute;
                    }

                }

                h1{
                    color: rgb(144, 0, 255);
                    padding-top: 0;
                    font-size: 36px;
                    text-shadow: 0px 0px 15px rgb(144, 0, 255);
                }

                .login-form{
                    width: 60%;
                    .input-container{
                        margin-top: 30px;
                    }
                    .customButtom{
                        margin-top: 30px;
                        color: white;
                        font-size: large;
                        font-weight: bold;
                        background-color: black;
                        border-radius: 3px;
                        border-width: 0;
                        width: 100%;
                        height: 15%;
                        transition: 0.5s;

                        &:hover{
                            cursor: pointer;
                            box-shadow: 0px 0px 15px rgb(144, 0, 255);
                            background-color: rgb(144, 0, 255);
                            transform: scale(1.1);
                        }

                    }
                }
            }
        }
    }

</style>