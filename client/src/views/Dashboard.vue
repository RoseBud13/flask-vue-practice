<template>
    <div>
        <el-row :gutter="20">
            <el-col :span="8">
                <el-card shadow="hover" class="mgb20" style="height:252px;">
                    <div class="user-info">
                        <img v-if="name == 'Team Koala'" src="../assets/img/koala.jpg" class="user-avator" />
                        <img v-else src="../assets/img/user.jpg" class="user-avator" />
                        <div class="user-info-cont">
                            <div class="user-info-name">{{ name }}</div>
                            <div>{{ role }}</div>
                        </div>
                    </div>
                    <div class="user-info-list">
                        Login Time：
                        <span>{{ time }}</span>
                    </div>
                    <div class="user-info-list">
                        Location：
                        <span>Volvo APHQ, Shanghai</span>
                    </div>
                </el-card>
                <div v-show="isAdmin">
                    <el-card shadow="hover" style="height:252px;">
                    <template #header>
                        <div class="clearfix">
                            <span>Sprint Story </span>
                        </div>
                    </template>
                    Vue
                    <el-progress :percentage="71.3" color="#42b983"></el-progress>
                    CIC RMS
                    <el-progress :percentage="64.1" color="#f1e05a"></el-progress>
                    Manual
                    <el-progress :percentage="83.7"></el-progress>
                    Gerrit
                    <el-progress :percentage="75.9" color="#f56c6c"></el-progress>
                </el-card>
                </div>
            </el-col>
            <el-col :span="16">
                <el-row :gutter="20" class="mgb20">
                    <el-col :span="8">
                        <el-card shadow="hover" :body-style="{ padding: '0px' }">
                            <div class="grid-content grid-con-1">
                                <i class="el-icon-s-opportunity grid-con-icon"></i>
                                <div class="grid-cont-right">
                                    <div class="grid-num">144301</div>
                                    <div>Total Issues</div>
                                </div>
                            </div>
                        </el-card>
                    </el-col>
                    <el-col :span="8">
                        <el-card shadow="hover" :body-style="{ padding: '0px' }">
                            <div class="grid-content grid-con-2">
                                <i class="el-icon-s-promotion grid-con-icon"></i>
                                <div class="grid-cont-right">
                                    <div class="grid-num">321</div>
                                    <div>{{ name }}</div>
                                </div>
                            </div>
                        </el-card>
                    </el-col>
                    <el-col :span="8">
                        <el-card shadow="hover" :body-style="{ padding: '0px' }">
                            <div class="grid-content grid-con-3">
                                <i class="el-icon-s-data grid-con-icon"></i>
                                <div class="grid-cont-right">
                                    <div class="grid-num">5000</div>
                                    <div>Activity</div>
                                </div>
                            </div>
                        </el-card>
                    </el-col>
                </el-row>
                <div v-show="isAdmin">
                    <el-card shadow="hover" style="height:403px;">
                        <template #header>
                            <div class="clearfix">
                                <span>Todos</span>
                                <el-button style="float: right; padding: 3px 0" type="text">Add</el-button>
                            </div>
                        </template>

                        <el-table :show-header="false" :data="todoList" style="width:100%;">
                            <el-table-column width="40">
                                <template #default="scope">
                                    <el-checkbox v-model="scope.row.status"></el-checkbox>
                                </template>
                            </el-table-column>
                            <el-table-column>
                                <template #default="scope">
                                    <div
                                        class="todo-item"
                                        :class="{
                                            'todo-item-del': scope.row.status,
                                        }"
                                    >{{ scope.row.title }}</div>
                                </template>
                            </el-table-column>
                            <el-table-column width="60">
                                <template>
                                    <i class="el-icon-edit"></i>
                                    <i class="el-icon-delete"></i>
                                </template>
                            </el-table-column>
                        </el-table>
                    </el-card>
                </div>
            </el-col>
        </el-row>
        <div v-show="isAdmin">
            <el-row :gutter="20">
                <el-col :span="12">
                    <el-card shadow="hover">
                        <schart ref="bar" class="schart" canvasId="bar" :options="options"></schart>
                    </el-card>
                </el-col>
                <el-col :span="12">
                    <el-card shadow="hover">
                        <schart ref="line" class="schart" canvasId="line" :options="options2"></schart>
                    </el-card>
                </el-col>
            </el-row>
        </div>
    </div>
</template>

<script>
import Schart from "vue-schart";
export default {
    name: "dashboard",
    data() {
        return {
            time: this.formatTime(),
            name: localStorage.getItem("ms_username"),
            todoList: [
                {
                    title: "Shell task integration",
                    status: true
                },
                {
                    title: "Zuul automation MVP",
                    status: true
                },
                {
                    title: "Artifactory usage manual",
                    status: true
                },
                {
                    title: "CarPort APK handling",
                    status: true
                },
                {
                    title: "CIC RMS prestudy",
                    status: false
                },
                {
                    title: "Flask",
                    status: false
                }
            ],
            data: [
                {
                    name: "2018/09/04",
                    value: 1083
                },
                {
                    name: "2018/09/05",
                    value: 941
                },
                {
                    name: "2018/09/06",
                    value: 1139
                },
                {
                    name: "2018/09/07",
                    value: 816
                },
                {
                    name: "2018/09/08",
                    value: 327
                },
                {
                    name: "2018/09/09",
                    value: 228
                },
                {
                    name: "2018/09/10",
                    value: 1065
                }
            ],
            options: {
                type: "bar",
                title: {
                    text: "Sprint 4"
                },
                xRorate: 25,
                labels: ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7", "Day 8"],
                datasets: [
                    {
                        label: "Julia",
                        data: [0, 2, 3, 5, 2, 0, 0, 0]
                    },
                    {
                        label: "Zhou",
                        data: [0, 1, 2, 4, 4, 3, 7, 10]
                    },
                    {
                        label: "Sean",
                        data: [0, 2, 0, 0, 0, 0, 4, 0]
                    },
                    {
                        label: "Kaijie",
                        data: [0, 6, 0, 1, 10, 2, 3, 0]
                    }
                ]
            },
            options2: {
                type: "line",
                title: {
                    text: "Sprint 4 Burndown Chart"
                },
                labels: ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7", "Day 8"],
                datasets: [
                    {
                        label: 'Plan',
                        data: [88, 88, 88, 90, 90, 90, 90, 93]
                    },
                    {
                        label: 'Burndown',
                        data: [88, 77, 72, 64, 48, 43, 29, 22]
                    },
                    {
                        label: 'Progress',
                        data: [0, 11, 5, 8, 16, 5, 14, 7]
                    }
                ]
            }
        };
    },
    components: {
        Schart
    },
    computed: {
        role() {
            return this.name === "Team Koala" ? "Admin" : "User";
        },
        isAdmin(){
            return this.name === "Team Koala" ? true : false;
        }
    },
    methods: {
        formatTime(timestamp) {
            var Y, m, d, H, i, s, result;
            var date;
            if (timestamp) {
                date = new Date(timestamp);
            } else {
                date = new Date();
            }
            Y = date.getFullYear(),
            m = date.getMonth() + 1,
            d = date.getDate(),
            H = date.getHours(),
            i = date.getMinutes(),
            s = date.getSeconds();
            if (m < 10) {
                m = '0' + m;
            }
            if (d < 10) {
                d = '0' + d;
            }
            if (H < 10) {
                H = '0' + H;
            }
            if (i < 10) {
                i = '0' + i;
            }
            if (s < 10) {
                s = '0' + s;
            }
            result = Y + '-' + m + '-' + d + ' ' + H + ':' + i + ':' + s;
            // console.log(sresult);
            return result;
        },
    }
};
</script>

<style scoped>
.el-row {
    margin-bottom: 20px;
}

.grid-content {
    display: flex;
    align-items: center;
    height: 100px;
}

.grid-cont-right {
    flex: 1;
    text-align: center;
    font-size: 14px;
    color: #999;
}

.grid-num {
    font-size: 30px;
    font-weight: bold;
}

.grid-con-icon {
    font-size: 50px;
    width: 100px;
    height: 100px;
    text-align: center;
    line-height: 100px;
    color: #fff;
}

.grid-con-1 .grid-con-icon {
    background: rgb(45, 140, 240);
}

.grid-con-1 .grid-num {
    color: rgb(45, 140, 240);
}

.grid-con-2 .grid-con-icon {
    background: rgb(100, 213, 114);
}

.grid-con-2 .grid-num {
    color: rgb(45, 140, 240);
}

.grid-con-3 .grid-con-icon {
    background: rgb(242, 94, 67);
}

.grid-con-3 .grid-num {
    color: rgb(242, 94, 67);
}

.user-info {
    display: flex;
    align-items: center;
    padding-bottom: 20px;
    border-bottom: 2px solid #ccc;
    margin-bottom: 20px;
}

.user-avator {
    width: 120px;
    height: 120px;
    border-radius: 50%;
}

.user-info-cont {
    padding-left: 50px;
    flex: 1;
    font-size: 14px;
    color: #999;
}

.user-info-cont div:first-child {
    font-size: 30px;
    color: #222;
}

.user-info-list {
    font-size: 14px;
    color: #999;
    line-height: 25px;
}

.user-info-list span {
    margin-left: 70px;
}

.mgb20 {
    margin-bottom: 20px;
}

.todo-item {
    font-size: 14px;
}

.todo-item-del {
    text-decoration: line-through;
    color: #999;
}

.schart {
    width: 100%;
    height: 300px;
}
</style>
