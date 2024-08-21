```csharp
namespace Project.Infrastructure.Domain.Brands
{
    public class BrandRepository : IBrandRepository
    {
        private readonly MultitenantContext _context;

        public BrandRepository(MultitenantContext context)
        { 
            _context = context; 
        }

        public async Task<Brand> CreateAsync(Brand entity)
        {
            var scheme = await _context.Brands.AddAsync(entity);
            return scheme.Entity;
        }

        public async Task<Brand?> GetByIdAsync(string id) =>
            await _context.Brands.FirstOrDefaultAsync(p => p.Id == id);

        public async Task<PaginatedResponse<Brand>> GetAllAsync(
            Specification<Brand>? specification = null, 
            OrderStrategy<Brand>? orderStrategy = null, 
            int? skip = null, 
            int? take = null)
        {
            var query = _context.Brands.AsQueryable();

            if (specification != null)
                query = query.Where(specification.ToExpression());

            if (orderStrategy != null)
                query = query.OrderByStrategy(orderStrategy);

            var totalResults = await query.CountAsync();

            if (skip != null)
                query = query.Skip(skip.Value);

            if (take != null)
                query = query.Take(take.Value);

            return new PaginatedResponse<Brand>
            {
                TotalResults = totalResults,
                Results = await query.ToListAsync()
            };
        }

        public Brand Update(Brand entity)
        {
            var scheme = _context.Brands.Update(entity);
            return scheme.Entity;
        }

        public Brand Delete(Brand entity)
        {
            var scheme = _context.Brands.Remove(entity);
            return scheme.Entity;
        }
    }
}
```