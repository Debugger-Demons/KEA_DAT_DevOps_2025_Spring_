   export async function seed(knex) {
     // Clear existing entries
     await knex('users').del();
   
     // Insert seed entries
     await knex('users').insert([
       { id: 1, first_name: 'John', last_name: 'Doe' },
       { id: 2, first_name: 'Jane', last_name: 'Smith' },
       { id: 3, first_name: 'Alice', last_name: 'Johnson' }
     ]);
   }

