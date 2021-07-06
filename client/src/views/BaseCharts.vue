<template>
    <div class="login-wrap">
        
        
    </div>
</template>

<script>

export default {
    name: 'basecharts',

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
.login-wrap {
    position: relative;
    width: 100%;
    height: 100%;
    background-image: url(../assets/img/data.png);
    background-size: 100%;
}
</style>