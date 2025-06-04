use torneo_calcio;
-- 1. Elenca tutti gli stadi.
select * FROM stadi;
-- 2. Visualizza il nome e la città di tutte le squadre.
select nome, citta from squadre;
-- 3. Elenca tutti i calciatori, mostrando nome e ruolo.
SELECT nome, ruolo from calciatori;
-- 4. Elenca tutti gli arbitri italiani.
select * from arbitri where nazionalita = "Italiana";
-- 5. Visualizza tutte le partite già terminate.
select * from partite;
-- 6. Elenca tutte le partite giocate allo Stadio Olimpico.
select p.* from stadi s
join partite p on s.id = p.stadio_id
where s.nome = "Stadio Olimpico";
-- 7. Trova i biglietti acquistati da “Mario Rossi”.
select * from biglietti b where b.nominativo = "Mario Rossi";
-- 8. Conta quante squadre ci sono nel database.
select COUNT(*) from squadre;
-- 9. Visualizza il nome e la capienza di tutti gli stadi, ordinati per capienza decrescente.
select nome, capienza from stadi order by capienza desc;
-- 10. Trova il nome e il cognome degli allenatori nati dopo il 1980.
select nome, cognome from arbitri where year(data_nascita) >= 1980;

-- 1. Elenca tutte le partite indicando i nomi delle squadre di casa e trasferta.
select s1.nome, s2.nome from partite p
join squadre s1 on p.squadra_casa_id = s1.id
join squadre s2 on p.squadra_trasferta_id = s2.id;
-- 2. Trova i calciatori che giocano nell’“AS Roma”.
select c.nome, c.cognome from calciatori c
join squadre s on c.squadra_id = s.id
where s.nome = "AS Roma";
-- 3. Elenca tutte le partite arbitrate da “Daniele Orsato”.
select p.* from partite p
join arbitri a on p.arbitro_id = a.id
where a.nome = "Daniele" and a.cognome = "Orsato";
-- 4. Elenca per ogni partita il numero totale di biglietti venduti.
select COUNT(b.partita_id) from biglietti b
join partite p on b.partita_id = p.id
group by b.partita_id;
-- 5. Trova i marcatori della partita con id 1 (nome, cognome, minuto).
select c.nome, c.cognome, m.minuto  from marcatori m
join partite p on m.partita_id = p.id
join calciatori c on m.calciatore_id = c.id
where p.id = 1;
-- 6. Elenca i calciatori che hanno ricevuto almeno una sanzione.
select c.nome, c.cognome from sanzioni s
join calciatori c on s.calciatore_id = c.id
group by s.calciatore_id;