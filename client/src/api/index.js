import request from '../utils/request'

export function fetchResources(query) {
  return request({
    url: '/resources/',
    method: 'get',
    params: query
  })
}

export function addResource(data) {
  return request({
    url: '/resources/',
    method: 'post',
    data
  })
}

export function getResource(id) {
  return request({
    url: `/resources/${id}/`,
    method: 'get'
  })
}

export function deleteResource(id) {
  return request({
    url: `/resources/${id}/`,
    method: 'delete'
  })
}

export function updateResource(id, data) {
  return request({
    url: `/resources/${id}/`,
    method: 'put',
    data
  })
}
