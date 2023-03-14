import { createRouter, createWebHistory} from 'vue-router'
 
import InfoMain from '@/views/InfoMain.vue'
import LoginPage from '@/views/LoginPage.vue'
import AdminPage from '@/views/AdminPage.vue'
import AdminClaims from '@/views/admin/AdminClaims.vue'
import AdminDemands from '@/views/admin/AdminDemands.vue'
import AdminMain from '@/views/admin/AdminMain.vue'
import AdminNotice from '@/views/admin/AdminNotice.vue'
import AdminRents from '@/views/admin/AdminRents.vue'
import AdminStands from '@/views/admin/AdminStands.vue'
import AdminUsers from '@/views/admin/AdminUsers.vue'

const routes = [
    {
        path: '/',
        component: InfoMain
    },
    {
        path: '/login',
        component: LoginPage
    },
    {
        path: '/admin',
        component: AdminPage,
        children: [
            { path: '', component: AdminMain },
            { path: 'users', component: AdminUsers },
            { path: 'rents', component: AdminRents },
            { path: 'claims', component: AdminClaims },
            { path: 'stands', component: AdminStands },
            { path: 'demands', component: AdminDemands },
            { path: 'notice', component: AdminNotice }
        ]
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export { router }