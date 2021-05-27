<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item>
                    <i class="el-icon-lx-cascades"></i> Resources
                </el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="container">
            <el-table
                :data="resources"
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
                
                <el-table-column label="Status" align="center" width="110">
                    <template #default="scope">
                        <el-tag
                            :type="
                                scope.row.status === 'active'
                                    ? 'success'
                                    : scope.row.status === 'removed'
                                    ? 'danger'
                                    : scope.row.status === 'booked'
                                    ? 'danger'
                                    : ''
                            "
                        >{{ scope.row.status }}</el-tag>
                    </template>
                </el-table-column>

                <el-table-column prop="ci_level" label="CI Level" width="100"></el-table-column>

                <el-table-column prop="responsible_user" label="Responsible User"></el-table-column>

                <el-table-column prop="location" label="Location" width="80"></el-table-column>

                <el-table-column prop="description" label="Description"></el-table-column>

                <el-table-column prop="rsrc_type" label="Type" width="70"></el-table-column>

                <el-table-column label="Operation" width="230" align="center">
                    <template #default="scope">
                        <el-button
                            type="text"
                            icon="el-icon-s-order"
                            @click="handleBook(scope.$index, scope.row)"
                        >Book</el-button>
                        <el-button
                            type="text"
                            icon="el-icon-s-order"
                            @click="handleEdit(scope.$index, scope.row)"
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

        <!-- 编辑弹出框 -->
        <el-dialog title="Edit" v-model="editVisible" width="50%">
            <el-form ref="form" :model="rsrc" label-width="150px">
                <el-form-item label="Resource Name">
                    <el-input v-model="rsrc.rsrc_name"></el-input>
                </el-form-item>
                <el-form-item label="Department">
                    <el-input v-model="rsrc.department"></el-input>
                </el-form-item>
                <el-form-item label="CI Level">
                    <el-input v-model="rsrc.ci_level"></el-input>
                </el-form-item>
                <el-form-item label="Responsible User">
                    <el-input v-model="rsrc.responsible_user"></el-input>
                </el-form-item>
                <el-form-item label="Location">
                    <el-input v-model="rsrc.location"></el-input>
                </el-form-item>
                <el-form-item label="Description">
                    <el-input v-model="rsrc.description"></el-input>
                </el-form-item>
                <el-form-item label="Type">
                    <el-input v-model="rsrc.rsrc_type"></el-input>
                </el-form-item>
                <el-form-item label="Status">
                    <el-input v-model="rsrc.status"></el-input>
                </el-form-item>
            </el-form>
            <template #footer>
                <span class="dialog-footer">
                    <el-button id="volvo" @click="editVisible=false">Cancel</el-button>
                    <el-button id="volvo" @click="saveEdit">Confirm</el-button>
                </span>
            </template>
        </el-dialog>

        <!-- 预订弹出框 -->
        <el-dialog title="Book" v-model="bookVisible" width="50%">
            <el-form ref="form" :model="reservation" label-width="150px">
                <el-form-item label="Book for:">
                    <el-input v-model="reservation.booked_for_name"></el-input>
                </el-form-item>

                <el-form-item label="From">
                    <el-col :span="11">
                        <el-date-picker
                            type="date"
                            placeholder="Select date"
                            v-model="reservation.booked_from"
                            style="width: 100%;"
                        ></el-date-picker>
                    </el-col>
                    <el-col class="line" :span="2">- To</el-col>
                    <el-col :span="11">
                        <el-date-picker
                            type="date"
                            placeholder="Select date"
                            v-model="reservation.booked_until"
                            style="width: 100%;"
                        ></el-date-picker>
                    </el-col>
                </el-form-item>
                
                <el-form-item label="Description">
                    <el-input v-model="reservation.description"></el-input>
                </el-form-item>
            </el-form>
            <template #footer>
                <span class="dialog-footer">
                    <el-button id="volvo" @click="bookVisible=false">Cancel</el-button>
                    <el-button id="volvo" @click="saveBook">Confirm</el-button>
                </span>
            </template>
        </el-dialog>
    </div>
</template>

<script>
import { fetchResources, deleteResource, updateResource, addReservation } from '../api/index'

export default {
    name: "resources",
    data() {
        return {
            resources: [],
            editVisible: false,
            bookVisible: false,
            rsrc: {
                rsrc_name: '',
                department: '',
                ci_level: '',
                responsible_user: '',
                location: '',
                description: '',
                status: '',
                rsrc_type: ''
            },
            reservation: {
                booked_for_name: '',
                booked_by_name: 'Team Koala',
                booked_from: '',
                booked_util: '',
                description: ''
            },
            idx: -1,
            updatedRsrc: null
        };
    },
    created() {
        this.fetchData();
    },
    methods: {
        fetchData() {
            fetchResources().then(response => {
                console.log(response);
                this.resources = response.resources
            })
        },

        handleBook(index, row) {
            this.idx = index;
            this.bookVisible = true;
            this.rsrc = row;
        },

        saveBook() {
            let data = {
                booked_rsrc_name: this.rsrc.rsrc_name,
                booked_for_name: this.reservation.booked_for_name,
                booked_by_name: this.reservation.booked_by_name,
                booked_from: this.reservation.booked_from,
                booked_until: this.reservation.booked_until,
                description: this.reservation.description
            }

            addReservation(data).then(() => {
                this.$message.success(`Book row ${this.idx + 1} succeed`);
            }).catch(e => {
                console.log(e)
            })

            this.updatedRsrc = {
                rsrc_name: this.rsrc.rsrc_name,
                department: this.rsrc.department,
                ci_level: this.rsrc.ci_level,
                responsible_user: this.rsrc.responsible_user,
                location: this.rsrc.location,
                description: this.rsrc.description,
                status: 'booked',
                rsrc_type: this.rsrc.rsrc_type
            }

            updateResource(this.rsrc.id, this.updatedRsrc)
            .then(() => {
                this.$message.success(`Update row ${this.idx + 1} succeed`);
            })
            .catch(e => {
                console.log(e);
            });

            this.bookVisible = false;

            this.$router.go(this.$router.currentRoute)
        },

        handleEdit(index, row) {
            this.idx = index;
            this.editVisible = true;
            this.rsrc = row;
        },

        saveEdit() {
            this.updatedRsrc = {
                rsrc_name: this.rsrc.rsrc_name,
                department: this.rsrc.department,
                ci_level: this.rsrc.ci_level,
                responsible_user: this.rsrc.responsible_user,
                location: this.rsrc.location,
                description: this.rsrc.description,
                status: this.rsrc.status,
                rsrc_type: this.rsrc.rsrc_type
            }
            updateResource(this.rsrc.id, this.updatedRsrc)
            .then(() => {
                this.$message.success(`Update row ${this.idx + 1} succeed`);
            })
            .catch(e => {
                console.log(e);
            });
            this.editVisible = false;
        },

        handleDelete(index, row) {
            this.$confirm('Confirm to remove this resource?', 'Warning', {
            confirmButtonText: 'Confirm',
            cancelButtonText: 'Cancel',
            type: 'warning'
        })
        .then(async() => {
            await deleteResource(row.id)
            this.resources.splice(index, 1)
            this.$message({
                type: 'success',
                message: 'Delete succeed!'
            })
        })
        .catch(err => { console.error(err) })
        },
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
