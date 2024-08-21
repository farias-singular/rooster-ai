```csharp
namespace Project.Application.UseCases.Brands.GetAllBrands
{
    public class GetAllBrandsHandler : IQueryHandler<GetAllBrandsQuery, PaginatedResponse<GetAllBrandsDto>>
    {
        private readonly IBrandRepository _brandRepository;
        private readonly IMapper _mapper;

        public GetAllBrandsHandler(
            IBrandRepository brandRepository, 
            IMapper mapper) 
        {
            _brandRepository = brandRepository;
            _mapper = mapper;
        }

        public async Task<PaginatedResponse<GetAllBrandsDto>> Handle(GetAllBrandsQuery query, CancellationToken ct = default)
        {
            var specifications = new List<Specification<Brand>>();

            if (!string.IsNullOrEmpty(query.BrandIdOrName))
                specifications.Add(new BrandIdOrNameSpecification(query.BrandIdOrName));

            if (query.BrandIds is not null)
                specifications.Add(new BrandIdIsContainedInSpecification(query.BrandIds));

            var specification = specifications.AggregateAnd();

            OrderStrategy<Brand> orderByStrategy = query.OrderBy switch
            {
                BrandOrderBy.Id => new OrderByIdStrategy(query.OrderByDescending ?? false),
                BrandOrderBy.Name => new OrderByNameStrategy(query.OrderByDescending ?? false),
                _ => new OrderByCreateDateStrategy(query.OrderByDescending ?? false)
            };

            var brands = await _brandRepository.GetAllAsync(
                specification,
                orderByStrategy,
                query.Offset, 
                query.Limit);

            return _mapper.Map<PaginatedResponse<GetAllBrandsDto>>(brands);
        }            
    }
}
```