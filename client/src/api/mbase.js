import mbaseRequest from '../utils/mbaseRequest'

export function fetchInfoData(query) {
    return mbaseRequest({
      url: '/hash/DSLS_gotsvl1144_Info',
      method: 'get',
      params: query
    })
  }
