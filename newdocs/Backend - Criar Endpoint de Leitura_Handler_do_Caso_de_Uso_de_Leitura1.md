```csharp
namespace Project.Application.UseCases.Brands.GetBrandById
{
    public class GetBrandByIdHandler : IQueryHandler<GetBrandByIdQuery, GetBrandByIdDto>
    {
        private readonly IBrandRepository _brandRepository;
        private readonly IMapper _mapper;

        public GetBrandByIdHandler(
            IBrandRepository brandRepository,
            IMapper mapper)
        {
            _brandRepository = brandRepository;
            _mapper = mapper;
        }

        public async Task<GetBrandByIdDto> Handle(GetBrandByIdQuery query, CancellationToken ct = default)
        {
            var brand = await _brandRepository.GetByIdAsync(query.Id);
            if (brand == null)
            {
                throw new NotFoundException("Brand not found");
            }

            return _mapper.Map<GetBrandByIdDto>(brand);
        }
    }
}
```