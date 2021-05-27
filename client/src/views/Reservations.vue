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
                            @click="handleEditRsvt(scope.$index, scope.row)"
                        >Edit</el-button>
                        <el-button
                            type="text"
                            icon="el-icon-delete"
                            class="red"
                            @click="handleDeleteRsvt(scope.$index, scope.row)"
                        >Delete</el-button>
                    </template>
                </el-table-column>
            </el-table>
        </div>

        <!-- 编辑弹出框 -->
        <el-dialog title="Edit" v-model="editVisible" width="50%">
            <el-form ref="form" :model="rsvt" label-width="150px">
                <el-form-item label="Book for:">
                    <el-input v-model="rsvt.booked_for_name"></el-input>
                </el-form-item>
                <el-form-item label="Start Date">
                    <el-input v-model="rsvt.booked_from"></el-input>
                </el-form-item>
                <el-form-item label="End Date">
                    <el-input v-model="rsvt.booked_until"></el-input>
                </el-form-item>
                <el-form-item label="Description">
                    <el-input v-model="rsvt.description"></el-input>
                </el-form-item>
            </el-form>
            <template #footer>
                <span class="dialog-footer">
                    <el-button id="volvo" @click="editVisible=false">Cancel</el-button>
                    <el-button id="volvo" @click="saveEditRsvt">Confirm</el-button>
                </span>
            </template>
        </el-dialog>
    </div>
</template>

<script>
import { fetchReservations, updateReservation, cancelReservation } from '../api/index'

export default {
    name: "reservations",
    data() {
        return {
            reservations: [],
            editVisible: false,
            rsvt: {
                booked_src_name: '',
                booked_for_name: '',
                booked_by_name: '',
                booked_from_date: '',
                booked_until_date: '',
                description: ''
            },
            updatedRsvt: null
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

        handleEditRsvt(index, row) {
            this.idx = index;
            this.editVisible = true;
            this.rsvt = row;
        },

        saveEditRsvt() {
            this.updatedRsvt = {
                booked_src_name: this.rsvt.booked_src_name,
                booked_for_name: this.rsvt.booked_for_name,
                booked_by_name: this.rsvt.booked_by_name,
                booked_from_date: this.rsvt.booked_from_date,
                booked_until_date: this.rsvt.booked_until_date,
                description: this.rsvt.description
            }
            updateReservation(this.rsvt.id, this.updatedRsvt)
            .then(() => {
                this.$message.success(`Update row ${this.idx + 1} succeed`);
            })
            .catch(e => {
                console.log(e);
            });
            this.editVisible = false;
        },

        handleDeleteRsvt(index, row) {
            this.$confirm('Confirm to remove this resource?', 'Warning', {
            confirmButtonText: 'Confirm',
            cancelButtonText: 'Cancel',
            type: 'warning'
        })
        .then(async() => {
            await cancelReservation(row.id)
            this.reservations.splice(index, 1)
            this.$message({
                type: 'success',
                message: 'Delete succeed!'
            })
        })
        .catch(err => { console.error(err) })
        },
    }
}
</script>
