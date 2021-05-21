<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item>
                    <i class="el-icon-lx-calendar"></i> Add
                </el-breadcrumb-item>
                <el-breadcrumb-item>Add Resource</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div v-if="!added">
            <div class="container">
            <div class="form-box">
                <el-form ref="Resource" :model="Resource" label-width="80px">
                    <el-form-item label="Name" required>
                        <el-input v-model="Resource.rsrc_name"></el-input>
                    </el-form-item>
                    <el-form-item label="Type" required>
                        <el-select v-model="Resource.rsrc_type" placeholder="Please select">
                            <el-option key="hil" label="HIL" value="hil"></el-option>
                            <el-option key="bc" label="Boxcar" value="boxcar"></el-option>
                            <el-option key="tb" label="Test Bench" value="test bench"></el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item label="Status" required>
                        <el-select v-model="Resource.status" placeholder="Please select">
                            <el-option key="ac" label="active" value="active"></el-option>
                            <el-option key="rm" label="removed" value="removed"></el-option>
                            <el-option key="m" label="maintanence" value="maintanence"></el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item label="Description" required>
                        <el-input type="textarea" rows="5" v-model="Resource.description"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="createResource">Submit</el-button>
                        <el-button @click="added=true">Cancel</el-button>
                    </el-form-item>
                </el-form>
            </div>
        </div>
        </div>
        <div v-else>
            <h4>You added successfully!</h4>
            <el-button type="primary" @click="newAdd">Add</el-button>
        </div>
    </div>
</template>

<script>
import { addResource } from '../api/index'

export default {
    name: 'addResource',
    emits: ['click'],
    data() {
        return {
            Resource: {
                rsrc_name: '',
                rsrc_type: '',
                description: '',
                status: ''
            },
            added: false,
        };
    },
    methods: {
        createResource() {
            let data = {
                rsrc_name: this.Resource.rsrc_name,
                status: this.Resource.status,
                description: this.Resource.description,
                rsrc_type: this.Resource.rsrc_type
            }
            addResource(data).then(response => {
                console.log(response);
                this.added = true;
            }).catch(e => {
                console.log(e)
            })
        },
        newAdd() {
            this.added = false;
            this.Resource = {};
        }
    },
};
</script>
