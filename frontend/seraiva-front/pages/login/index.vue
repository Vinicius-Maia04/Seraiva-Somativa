<script setup>

</script>

<template>
    <section class="screen-1">
        <section class="login-panel">
            <div class="login-content flex-center" >
                <form class="login-form">
                    <div class="input-container">
                        <CustomInput type="email" label="LOGIN" inputId="user-login"/>
                    </div>
                    <div class="input-container">
                        <CustomInput type="password" label="SENHA" inputId="pass-login"/>
                    </div>
                    <button type="submit" class="customButtom">Entrar</button>
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
                        background-color: rgb(144, 0, 255);
                        border-radius: 3px;
                        border-width: 0;
                        width: 100%;
                        height: 15%;

                    }
                }
            }
        }
    }

</style>