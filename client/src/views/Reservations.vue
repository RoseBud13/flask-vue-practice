<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item>
                    <i class="el-icon-lx-cascades"></i> Reservations
                </el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="container">
            <el-table
                :data="reservations"
                border
                stripe
                class="table"
                ref="multipleTable"
                header-cell-class-name="table-header"
                style="width: 100%"
            >

                <el-table-column prop="id" label="ID" width="55" align="center"></el-table-column>

                <el-table-column prop="booked_rsrc_name" label="Resource Name"></el-table-column>

                <el-table-column prop="booked_for_name" label="User"></el-table-column>

                <el-table-column prop="booked_by_name" label="Booked By"></el-table-column>

                <el-table-column prop="booked_from" label="Start Date"></el-table-column>

                <el-table-column prop="booked_until" label="End Date"></el-table-column>

                <el-table-column prop="description" label="Description"></el-table-column>

                <el-table-column label="Operation" width="200" align="center">
                    <template #default="scope">
                        <el-button
                            type="text"
                            icon="el-icon-s-order"
                            @click="handleReservation(scope.$index, scope.row)"
                        >Edit</el-button>
                        <el-button
                            type="text"
                            icon="el-icon-delete"
                            class="red"
                            @click="handleDelete(scope.$index, scope.row)"
                        >Delete</el-button>
                    </template>
                </el-table-column>
            </el-table>
        </div>
    </div>
</template>

<script>
import { fetchReservations } from '../api/index'

export default {
    name: "reservations",
    data() {
        return {
            reservations: []
        }
    },
    created() {
        this.fetchData();
    },
    methods: {
        fetchData() {
            fetchReservations().then(response => {
                console.log(response);
                this.reservations = response.reservations
            })
        },
    }
}
</script>
