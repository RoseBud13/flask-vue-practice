<template>
    <div>
        {{ infodata }}
        <!-- <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item>
                    <i class="el-icon-lx-cascades"></i> Resources
                </el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="container">
            <el-table
                :data="infodata"
                border
                stripe
                class="table"
                ref="multipleTable"
                header-cell-class-name="table-header"
                style="width: 100%"
            >

                <el-table-column prop="id" label="ID" width="55" align="center"></el-table-column>

                <el-table-column prop="rsrc_name" label="Resource Name"></el-table-column>

                <el-table-column prop="department" label="Department"></el-table-column>

                <el-table-column prop="ci_level" label="CI Level" width="100"></el-table-column>

                <el-table-column prop="responsible_user" label="Responsible User"></el-table-column>

                <el-table-column prop="location" label="Location" width="80"></el-table-column>

                <el-table-column prop="description" label="Description"></el-table-column>

                <el-table-column prop="rsrc_type" label="Type" width="70"></el-table-column>

            </el-table>
        </div> -->
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: "mbase",
    data() {
        return {
            infodata: null
        };
    },
    mounted () {
    axios
      .get('https://api.coindesk.com/v1/bpi/currentprice.json')
      .then(response => (this.infodata = response))
  }
};
</script>

<style scoped>
.handle-box {
    margin-bottom: 20px;
}

.handle-select {
    width: 120px;
}

.handle-input {
    width: 300px;
    display: inline-block;
}
.table {
    width: 100%;
    font-size: 14px;
}
.red {
    color: #ff0000;
}
.mr10 {
    margin-right: 10px;
}
.table-td-thumb {
    display: block;
    margin: auto;
    width: 40px;
    height: 40px;
}
</style>
