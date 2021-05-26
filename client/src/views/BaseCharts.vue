<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item>
                    <i class="el-icon-pie-chart"></i> Data
                </el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="container">
            <div class="schart-box">
                <div class="content-title">Test Cases</div>
                <schart class="schart" canvasId="bar" :options="options1"></schart>
            </div>
            <div class="schart-box">
                <div class="content-title">Bugs</div>
                <schart class="schart" canvasId="line" :options="options2"></schart>
            </div>
        </div>
    </div>
</template>

<script>
import Schart from 'vue-schart';
export default {
    name: 'basecharts',
    components: {
        Schart
    },
    data() {
        return {
            options1: {
                type: 'bar',
                title: {
                    text: 'Test Case Performed'
                },
                bgColor: '#fbfbfb',
                labels: ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7", "Day 8"],
                datasets: [
                    {
                        label: '522A',
                        data: [0, 2, 3, 5, 2, 0, 0, 0]
                    },
                    {
                        label: '622A',
                        data: [0, 1, 2, 4, 4, 3, 7, 10]
                    },
                    {
                        label: 'V536',
                        data: [0, 2, 0, 0, 0, 0, 4, 0]
                    },
                    {
                        label: 'V519',
                        data: [0, 6, 0, 1, 10, 2, 3, 0]
                    }
                ]
            },
            options2: {
                type: 'line',
                title: {
                    text: 'Issue Fixed'
                },
                bgColor: '#fbfbfb',
                labels: ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7", "Day 8"],
                datasets: [
                    {
                        label: 'Total',
                        data: [88, 88, 88, 90, 90, 90, 90, 93]
                    },
                    {
                        label: 'Remain',
                        data: [88, 77, 72, 64, 48, 43, 29, 22]
                    },
                    {
                        label: 'Progress',
                        data: [0, 11, 5, 8, 16, 5, 14, 7]
                    }
                ]
            },
            options3: {
                type: 'pie',
                title: {
                    text: 'User Story Points'
                },
                legend: {
                    position: 'left'
                },
                bgColor: '#fbfbfb',
                labels: ['Training & User manual', 'Prestudy of Carport', 'Vcats', 'Zuul automation', 'Deploy toolchain', 'CIC RMS', 'Boxcar', 'Network issue'],
                datasets: [
                    {
                        data: [7, 6, 11, 8, 4, 21, 9, 9]
                    }
                ]
            },
            options4: {
                type: 'ring',
                title: {
                    text: 'Points per member'
                },
                showValue: false,
                legend: {
                    position: 'bottom',
                    bottom: 40
                },
                bgColor: '#fbfbfb',
                labels: ['Julia', 'Sean', 'Zhou', 'Kaijie'],
                datasets: [
                    {
                        data: [13, 8, 43, 27]
                    }
                ]
            }
        };
    }
};
</script>

<style scoped>
.schart-box {
    display: inline-block;
    margin: 20px;
}
.schart {
    width: 600px;
    height: 400px;
}
.content-title {
    clear: both;
    font-weight: 400;
    line-height: 50px;
    margin: 10px 0;
    font-size: 22px;
    color: #1f2f3d;
}
</style>