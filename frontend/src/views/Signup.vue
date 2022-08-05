<template>

    <div id="grid">
        <div id="signup">
            <h3>Sign Up</h3>
            <form>
                <div class="form-elem">
                    <span>User Name：</span>
                    <input v-model="signupName" type="text" placeholder="Enter User Name">
                </div>

                <div class="form-elem">
                    <span>Password：</span>
                    <input v-model="signupPwd" type="password" placeholder="Enter Password">
                </div>

                <div class="form-elem">
                    <router-link :to="{ name: 'Login'}">Log in ...</router-link>
                </div>

                <div class="form-elem">
                    <button v-on:click.prevent="signup">Submit</button>
                </div>
            </form>
        </div>
    </div>

    <BlogFooter/>

</template>

<script>
    import axios from 'axios';
    import BlogFooter from '@/components/BlogFooter.vue'


    export default {
        name: 'Signup',
        components: {BlogFooter},
        data: function () {
            return {
                signupName: '',
                signupPwd: '',
                signupResponse: null,
            }
        },
        methods: {
            signup() {
                const that = this;
                axios
                    .post('/api/user/', {
                        username: this.signupName,
                        password: this.signupPwd,
                    })
                    .then(function (response) {
                        that.signupResponse = response.data;
                        alert('User registration is successful, please log in!');
                    })
                    .catch(function (error) {

                        alert(error.message);

                        // Handling Error here...

                        // https://github.com/axios/axios#handling-errors

                    });
            },
        }
    }
</script>

<style scoped>

    #grid {
        display: grid;
        grid-template-columns: 1fr;
    }

    #signup {
        text-align: center;
    }

    .form-elem {
        padding: 10px;
    }

    input {
        height: 25px;
        padding-left: 10px;
    }

    button {
        height: 35px;
        cursor: pointer;
        border: none;
        outline: none;
        background: gray;
        color: whitesmoke;
        border-radius: 5px;
        width: 60px;
    }
</style>