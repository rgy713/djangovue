<template>
    <div id="grid">
        <div id="signin">
            <h3>Log In</h3>
            <form>
                <div class="form-elem">
                    <span>User Name：</span>
                    <input v-model="signinName" type="text" placeholder="Enter user name">
                </div>

                <div class="form-elem">
                    <span>Password：</span>
                    <input v-model="signinPwd" type="password" placeholder="Enter password">
                </div>

                <div class="form-elem">
                    <router-link :to="{ name: 'Signup'}">Sign up ...</router-link>
                </div>

                <div class="form-elem">
                    <button v-on:click.prevent="signin">Submit</button>
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
        name: 'Login',
        components: {BlogFooter},
        data: function () {
            return {
                signinName: '',
                signinPwd: '',
            }
        },
        methods: {
            signin() {
                const that = this;
                axios
                    .post('/api/token/', {
                        username: that.signinName,
                        password: that.signinPwd,
                    })
                    .then(function (response) {
                        const storage = localStorage;
                        // Date.parse(...) 返回1970年1月1日UTC以来的毫秒数
                        const expiredTime = Date.parse(response.headers.date) + 60 * 100 * 1000;
                        // 设置 localStorage
                        storage.setItem('access.myblog', response.data.access);
                        storage.setItem('refresh.myblog', response.data.refresh);
                        storage.setItem('expiredTime.myblog', expiredTime);
                        storage.setItem('username.myblog', that.signinName);

                        // 是否为管理员
                        axios
                            .get('/api/user/' + that.signinName + '/')
                            .then(function (response) {
                                storage.setItem('isSuperuser.myblog', response.data.is_superuser);
                                storage.setItem('userId.myblog', response.data.id);
                                // 路由跳转
                                that.$router.push({name: 'Home'});
                            });
                            // .catch(...)
                    })
                // .catch(...)
            },
        }
    }
</script>

<style scoped>

    #grid {
        display: grid;
        grid-template-columns: 1fr;
    }

    #signin {
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