<template>
    <div class="header">
        <div class="header-left">
            <!-- 折叠按钮 -->
            <div class="collapse-btn" @click="collapseChage">
                <i v-if="!collapse" class="el-icon-s-fold"></i>
                <i v-else class="el-icon-s-unfold"></i>
            </div>
            <div class="volvo-logo">
                <img src="../assets/img/volvo-wordmark-black.svg" alt="volvo">
            </div>
            <div class="title">Resource Allocation System</div>
        </div>
        <div class="header-right">
            <div class="header-user-con">
                <!-- 消息中心 -->
                <div class="btn-bell">
                    <el-tooltip
                        effect="dark"
                        :content="message?`${message}unread messages`:`Messages`"
                        placement="bottom"
                    >
                        <router-link to="/messages">
                            <i class="el-icon-bell"></i>
                        </router-link>
                    </el-tooltip>
                    <span class="btn-bell-badge" v-if="message"></span>
                </div>
                <!-- 用户头像 -->
                <div class="user-avator">
                    <img v-if="username == 'Team Koala'" src="../assets/img/koala.jpg" />
                    <img v-else src="../assets/img/user.jpg" />
                </div>
                <!-- 用户名下拉菜单 -->
                <el-dropdown class="user-name" trigger="click" @command="handleCommand">
                    <span class="el-dropdown-link">
                        {{username}}
                        <i class="el-icon-caret-bottom"></i>
                    </span>
                    <template #dropdown>
                        <el-dropdown-menu>
                            <a href="https://github.com/RoseBud13/flask-vue-practice" target="_blank">
                                <el-dropdown-item>Source Code</el-dropdown-item>
                            </a>
                            <el-dropdown-item divided command="loginout">Logout</el-dropdown-item>
                        </el-dropdown-menu>
                    </template>
                </el-dropdown>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    data() {
        return {
            fullscreen: false,
            name: 'kaijie',
            message: 2
        };
    },
    computed: {
        username() {
            let username = localStorage.getItem("ms_username");
            return username ? username : this.name;
        },
        collapse() {
            return this.$store.state.collapse;
        }
    },
    methods: {
        // 用户名下拉菜单选择事件
        handleCommand(command) {
            if (command == "loginout") {
                localStorage.removeItem("ms_username");
                this.$router.push("/login");
            }
        },
        // 侧边栏折叠
        collapseChage() {
            this.$store.commit("hadndleCollapse", !this.collapse);
        }
    },
    mounted() {
        if (document.body.clientWidth < 1500) {
            this.collapseChage();
        }
    }
};
</script>
<style scoped>
.header {
    position: relative;
    box-sizing: border-box;
    width: 100%;
    height: 70px;
    font-size: 22px;
    color: black;
}
.header-left {
    float: left;
    display: flex;
}
.collapse-btn {
    padding: 0 21px;
    cursor: pointer;
    line-height: 70px;
}
.header .title {
    width: 300px;
    line-height: 70px;
    font-weight: 700;
}
.header .volvo-logo {
    line-height: 70px;
    margin-right: 21px;
}
.header .volvo-logo img {
    width: 220px;
    height: 70px;
}
.header-right {
    float: right;
    padding-right: 50px;
}
.header-user-con {
    display: flex;
    height: 70px;
    align-items: center;
}
.btn-fullscreen {
    transform: rotate(45deg);
    margin-right: 5px;
    font-size: 24px;
}
.btn-bell,
.btn-fullscreen {
    position: relative;
    width: 30px;
    height: 30px;
    text-align: center;
    border-radius: 15px;
    cursor: pointer;
}
.btn-bell-badge {
    position: absolute;
    right: 0;
    top: -2px;
    width: 8px;
    height: 8px;
    border-radius: 4px;
    background: #f56c6c;
    color: black;
}
.btn-bell .el-icon-bell {
    color: black;
}
.user-name {
    margin-left: 10px;
}
.user-avator {
    margin: 0 20px;
}
.user-avator img {
    display: block;
    width: 40px;
    height: 40px;
    border-radius: 50%;
}
.el-dropdown-link {
    color: black;
    cursor: pointer;
}
.el-dropdown-menu__item {
    text-align: center;
}
</style>
